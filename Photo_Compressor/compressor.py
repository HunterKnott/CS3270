import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import hilbert

# Calculate Discrete Cosine Transform coefficient matrix
# Takes matrix length n as parameter
def DCT(n):
    C = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            C[i - 1, j - 1] = np.cos((i - 1) * (2 * j - 1) * np.pi / (2 * n))

    C = np.sqrt(2 / n) * C
    C[0, :] = C[0, :] / np.sqrt(2)

    return C

# Calculate Linear Quantization matrix
# Takes in loss parameter p to determine compression degree
def quant(p):
    Q = p * 8 / hilbert(8)
    return Q

# Compress the image data for RGB blocks of data
# Takes data block (X), DCT matrix (C), and quantization matrix (Q)
def compress(X, C, Q):
    Yq = np.zeros_like(X, dtype=np.float64)
    
    for color in range(3):  # Iterate over the colors R, G, B
        Xd = X[:, :, color].astype(np.float64)
        Xc = Xd - 128
        Y = np.dot(np.dot(C, Xc), C.T)
        Yq[:, :, color] = np.round(Y / Q)

    return Yq

# Decompress the image data for RGB blocks to get processed image data
# Takes compressed data block (Yq), DCT matrix (C), and quant. matrix (Q)
def decompress(Yq, C, Q):
    Xf = np.zeros_like(Yq, dtype=np.uint8)

    for color in range(3):  # Iterate over the colors R, G, B
        Ydq = Yq[:, :, color] * Q
        Xdq = np.dot(np.dot(C.T, Ydq), C)
        Xe = Xdq + 128
        Xf[:, :, color] = np.uint8(Xe)

    return Xf

def main():
    image = 'DSC_1994a.tif'
    print('Display image:', image)
    original = cv2.imread(image)

    # Convert the image from BGR to RGB (matplotlib uses RGB)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    # Display the image using matplotlib
    plt.imshow(original)
    plt.axis('off')  # Turn off axis labels
    plt.show()

    # Get image dimensions
    block_size = 8
    rows, cols, _ = original.shape

    # Edit and display the loss parameter p to adjust compression degree
    p = 32
    print('Loss Degree (p):', p)

    # Initialize result image
    result = np.zeros((rows, cols, 3), dtype=np.uint8)

    # Loop through the image in blocks of the specified size
    for row in range(0, rows, block_size):
        for col in range(0, cols, block_size):
            # Extract a single block to process
            block_row = slice(row, min(row + block_size, rows))
            block_col = slice(col, min(col + block_size, cols))
            X1 = original[block_row, block_col, :]

            # Get DCT matrix
            n = block_size
            DCTMatrix = DCT(n)

            # Get quantization matrix by using loss parameter (p)
            Q = quant(p)

            # Compress and then decompress the block
            Yq = compress(X1, DCTMatrix, Q)
            Xf = decompress(Yq, DCTMatrix, Q)

            # Put the block back into the result image
            result[block_row, block_col, :] = Xf
    
    # Show the result color image
    plt.imshow(result)
    plt.title('Processed Color Image')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()