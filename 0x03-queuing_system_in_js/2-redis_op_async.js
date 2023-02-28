import * as redis from 'redis';


const client = redis.createClient({
    url: 'redis://127.0.0.1:6379'
    });

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

/* (async () => {
    // Connect to redis server
    await client.connect();
})(); */

async function setNewSchool(schoolName, value){
  await client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName){
  await client.get(schoolName, (err, data) =>{
    if(err){
      console.log(err)
      throw err
    }
    console.log(data)
  })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');