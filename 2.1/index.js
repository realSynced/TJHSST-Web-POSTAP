/* 
1. Given a string of digits as an argument, write the function string_sum( str ) that computes the sum of all of 
the digits in the string. (Hint: Use Array.from( ) )
*/

function string_sum(str) {
  const numArr = str.split("");
  let sum = 0;
  numArr.forEach((num) => (sum += Number(num)));
  return sum;
}

/*
2. Given an array of numbers as an argument, write the function keep_evens( arr ) that returns just the even
digits within the Array. (Hint: Use .filter() )
*/

function keep_evens(arr) {
  const evenNums = arr.filter((num) => num % 2 === 0);
  return evenNums;
}

/*
3. Given the following array, write a filter function that keeps only objects where the age key is greater
than 40.
*/

function olderThan40(obj) {
  let newObjs = [];
  obj.map((obj) => {
    if (obj.age > 40) {
      newObjs.push(obj);
    }
  });
  return newObjs;
}

/*
4. Given an array of digits, write the function find_max ( arr ) that returns the maximum value from the Array.
*/

function find_max(arr) {
  let max = 0;
  arr.forEach((num) => {
    if (num > max) {
      max = num;
    }
  });
  return max;
}

/*
5. Given an array of digits, write the function find_max_min ( arr ) that returns an object with the maximum
and minimum values from the array. ( i.e. something like { ‘max’ : 12, ‘min’ : 0 } )
*/

function find_max_min(arr) {
  let maxMin = {
    max: 0,
    min: 0,
  };
  maxMin.max = find_max(arr);
  maxMin.min = Math.min(...arr);
  return maxMin;
}

/*
6. Given an array of digits, write the function sum_double ( arr ) that returns double the sum of all of the
digits.
*/

function sum_double(arr) {
  const sumDouble = arr.map((num) => num * 2);
  let sum = 0;
  sumDouble.forEach((num) => (sum += num));
  return sum;
}

/*
7. Given an array of digits, write the function sum_double_evens ( arr ) that returns the double the sum of all of
the even digits.
*/

function sum_double_evens(arr) {
  const evenNums = arr.filter((num) => num % 2 === 0);
  const sumDouble = evenNums.map((num) => num * 2);
  let sum = 0;
  sumDouble.forEach((num) => (sum += num));
  return sum;
}

/*
8. Given a string, write the function capitalize_firsts ( str ) that capitalizes the first letter of every word in the
string.
*/

function capitalize_firsts(str) {
  return str
    .split(" ")
    .map((word) => word[0].toUpperCase() + word.slice(1))
    .join(" ");
}

/* 
9. Given a string, write the function longest_word ( str ) that returns the longest word in a string. Assume the
words are separated by spaces or periods, and there are no other non-letter characters (like
apostrophes, etc).
*/

function longest_word(str) {
  const splitter = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "." || str[i] === " ") {
      splitter = str[i];
    }
  }
  let words = str.split(splitter);
  let wordLens = [];
  words.forEach((word) => wordLens.push(word.length));
  let longest = Math.max(...wordLens);
  let shortest = Math.min(...wordLens);
  return words[wordLens.indexOf(longest)];
}

function shortest_word(str) {
  const splitter = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "." || str[i] === " ") {
      splitter = str[i];
    }
  }
  let words = str.split(splitter);
  let wordLens = [];
  words.forEach((word) => wordLens.push(word.length));
  let shortest = Math.min(...wordLens);
  return words[wordLens.indexOf(shortest)];
}

/*
10. Given a string, write the function longest_shortest_word ( str ) that returns an object containing the longest
and shortest words in the string. ( i.e. { ‘longest’ : ‘banana’, ‘shortest’ : ‘the } ). Assumptions as in #8.
*/

function longest_shortest_word(str) {
  return {
    longest: longest_word(str),
    shortest: shortest_word(str),
  };
}

/*
11. Given a string containing digits and other characters, write the function digits_only ( str ) that returns an
array containing only the digits from the string.
*/

function digits_only(str) {
  return str.split("").filter((char) => !isNaN(char) && char !== " ");
}
