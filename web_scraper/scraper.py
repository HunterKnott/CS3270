1. Return the first name and last name for the person with the area code equal to "952" and the phone number equal to "555-1095"?
contacts> db.contacts.find({
... area_code: { $eq: "952" },
... phone: { $eq: "555-1095" }
... })
[
  {
    _id: ObjectId('65c1559c29cdb3aba12fcee7'),
    contact_id: 10021,
    first_name: 'Joselin',
    last_name: 'Staton',
    area_code: '952',
    phone: '555-1095',
    email: 'Staton.Joselin-age@icloud.com'
  }
]
---------------------------------------
2. Find everyone where their last name starts with "Long"?
contacts> db.contacts.find( { last_name: { $regex: /^Long/ } } )
[
  {
    _id: ObjectId('65c1559c29cdb3aba12fcef5'),
    contact_id: 10030,
    first_name: 'Darchelle',
    last_name: 'Longley',
    area_code: '839',
    phone: '555-3170',
    email: 'Longley.Darchelle-prove@hotmail.com'
  },
  {
    _id: ObjectId('65c1559c29cdb3aba12fd176'),
    contact_id: 10663,
    first_name: 'Sonya',
    last_name: 'Long',
    area_code: '306',
    phone: '555-5763',
    email: 'Long.Sonya-odd@outlook.com'
  },
  {
    _id: ObjectId('65c1559c29cdb3aba12fd1fa'),
    contact_id: 10806,
    first_name: 'Faline',
    last_name: 'Longshore',
    area_code: '530',
    phone: '555-8848',
    email: 'Longshore.Faline-maryland@gmail.com'
  }
]
---------------------------------------
3. Update the first name to 'Kristiann' where first name equals 'Kristiana' and last name equals 'Lammers'?
contacts> db.contacts.updateOne( { "first_name": "Kristiana", "last_name": "Lammers" }, { $set: { "first_name": "Kristiann" } } );
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0
}
---------------------------------------
4. Find the person with the first name 'Jolie' and last name 'Mccrimmon'?
contacts> db.contacts.find({
... first_name: {$eq: "Jolie" },
... last_name: {$eq: "Mccrimmon" }
... })
[
  {
    _id: ObjectId('65c15fd1e23be760cc4cbc14'),
    contact_id: 10970,
    first_name: 'Jolie',
    last_name: 'Mccrimmon',
    area_code: '847',
    phone: '555-7786',
    email: 'Mccrimmon.Jolie-scotland@yahoo.com'
  }
]
---------------------------------------
5. Find the person with the email 'Marshal.Jonna-filters@yahoo.com'?
contacts> db.contacts.find({ email: "Marshal.Jonna-filters@yahoo.com" });
[
  {
    _id: ObjectId('65c15fd1e23be760cc4cbbcd'),
    contact_id: 10872,
    first_name: 'Jonna',
    last_name: 'Marshal',
    area_code: '551',
    phone: '555-2955',
    email: 'Marshal.Jonna-filters@yahoo.com'
  }
]
---------------------------------------
6. Update the email for the person with email 'Glasco.Javone-dx@gmail.com' to 'Glasco.Javone-dx@icloud.com'?
contacts> db.contacts.updateOne( { "email": "Glasco.Javone-dx@gmail.com"}, { $set: { "email": "Glasco.Javone-dx@icloud.com" } } );
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
---------------------------------------
7. Change the first name to 'Calvin' where the first name is 'Kalvin' and the last name is 'Calton'?
contacts> db.contacts.updateOne( { "first_name": "Kalvin", "last_name": "Calton"}, { $set: { "first_name": "Calvin" } } );
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
---------------------------------------
8. Delete the person with the first name 'Brihany' and the last name 'Strang'?
contacts> db.contacts.deleteOne( { first_name: { $eq: "Brihany" }, last_name: { $eq: "Strang" } } );
{ acknowledged: true, deletedCount: 1 }
---------------------------------------
9. Delete the person with the area code of "249", the phone number of '555-9934' and the last name of 'Falconer'?
contacts> db.contacts.deleteOne( { area_code: { $eq: "249" }, phone: { $eq: "555-9934" }, last_name: { $eq: "Falconer" } } );
{ acknowledged: true, deletedCount: 1 }
---------------------------------------
10. Insert yourself as a contact.
contacts> db.contacts.insertOne({"contact_id": 11001, "first_name": "Hunter", "last_name": "Knott", "areacode": "950", "phone": "123-4567", "email": "hunterknott00@gmail.com"});
{
  acknowledged: true,
  insertedId: ObjectId('65c1650799c7a8db69b37550')
}
contacts> db.contacts.find( { first_name: { $eq: "Hunter" }, last_name:
{ $eq: "Knott" } } );
[
  {
    _id: ObjectId('65c1650799c7a8db69b37550'),
    contact_id: 11001,
    first_name: 'Hunter',
    last_name: 'Knott',
    areacode: '950',
    phone: '123-4567',
    email: 'hunterknott00@gmail.com'
  }
]