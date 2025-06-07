// 1

const add = (a, b) => {
  return a + b;
};

// 2 --> Write the function makesTen as an arrow function. Given 2 ints, a and b, return True if one if them is
// 10 or if their sum is 10.

const makesTen = (a, b) => {
  return a === 10 || b === 10 || a + b === 10;
};

// 3 Given the following object, write the code that uses the destructuring assignment to create the variables school and year.

const student = {
  name: "Abraham Agbota",
  school: "Thomas Jefferson High School for Science and Technology",
  year: 12,
};

// 4
// The following function uses the + operator to concatenate strings. Modify the function so that it uses template literals instead.

const complimentCats = (name, numCats) => {
  return `Hello, ${name}. Did you know I have ${numCats} cats? It's a whole vibe.`;
};
