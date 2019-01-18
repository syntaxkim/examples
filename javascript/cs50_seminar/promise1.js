console.log('I am starting')

let x = setTimeout(function () {
  return 5;
}, 2000);

let y = x * 10

// While console.log(y) is executing, x is not defined.
console.log(y)