console.log('I am starting')

// setTimeout is a Web APIs function.
setTimeout(function callback(){
  console.log('I am the callback function called when time is out')
}, 5000)

console.log('I am the last function called')

// When setTimeout is called,
// it is popped off from JS runtime engine call stack while being executing.
// When done, it is added to task queue.
// Event loop monitors task queue; when call stack is empty,
// it pushes the first function in task queue onto the call stack.