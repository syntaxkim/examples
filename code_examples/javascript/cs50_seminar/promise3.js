console.log('I am starting')

let new_promise = new Promise( function (resolve, reject) {
  setTimeout(function () {
    resolve(5);
  }, 2000);
});

// Use then method instead of await.
new_promise.then(x => {
  y = x * 5;
  console.log(y)
})