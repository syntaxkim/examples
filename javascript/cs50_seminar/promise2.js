console.log('I am starting')

let new_promise = new Promise( function (resolve, reject) {
  setTimeout(function () {
    resolve(5);
  }, 2000);
});

async function mult (){
  // await is going to pause this asynchronous function.
  // and wait for new_promise to be executed.
  let x = await new_promise
  let y = x * 5
  console.log(y)
}
mult();