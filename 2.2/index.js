/*
1. Given some credit card number, eg.: 4321 - 1234 - 9876 - 5432

2. Double every other digit. (8) 3 (4) 1 - (2) 2 (6) 4 - (18) 8 (14) 6 - (10) 4 (6) 2

3. Add the digits - but treat any number 10 or greater as individual digits
   8+3+4+1 + 2+2+6+4 + 1+8+8+1+4+6 + 1+0+4+6+2 = 71

4. If the resultant sum is divisible by 10, the credit card is valid! Since this card sums to 71, it is
   invalid. Note that 4321 - 1234 - 9876 - 5431 is a valid credit card number. Why?
*/

function checkCardValidity1(str) {
  let cardType = checkCardType(str);
  if (cardType === false) return false;
  const seperator = checkSeparator(str);
  let possibleSeperators = "";
  if (seperator === "dash") {
    possibleSeperators = "-";
  } else if (seperator === "space") {
    possibleSeperators = " ";
  }
  console.log("String", str);
  let cardNums = str.split(possibleSeperators);
  console.log("Card Numbers", cardNums);
  for (let i = 1; i < cardNums.length - 1; i += 2) {
    cardNums[i] = cardNums[i] * 2;
  }
  console.log("Double digits", cardNums);
  let sum = 0;
  for (let i = 0; i < cardNums.length; i++) {
    if (cardNums[i] >= 10) {
      console.log("Greater than 10", cardNums[i]);
      console.log(
        "Add greater than 10 seperately",
        cardNums[i]
          .toString()
          .split("")
          .reduce((a, b) => Number(a) + Number(b))
      );
      sum += cardNums[i]
        .toString()
        .split("")
        .reduce((a, b) => Number(a) + Number(b));
    } else {
      sum += Number(cardNums[i]);
    }
  }
  console.log("Sum", sum);
  return {
    isValid: sum % 10 === 0,
    type: cardType,
  };
}

function checkSeparator(str) {
  let dash = false;
  let space = false;
  for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
      space = true;
    } else if (str[i] === "-") {
      dash = true;
    }
  }

  if (dash && space) {
    return "dash";
  } else if (dash) {
    return "dash";
  } else if (space) {
    return "space";
  }
  return false;
}

function checkCardType(str) {
  if (str[0] === "4" && str.length === 16) {
    return "Visa";
  } else if (
    str[0] + str[1] === "34" ||
    (str[0] + str[1] === "37" && str.length === 15)
  ) {
    return "American Express";
  } else if (
    ["51", "52", "53", "54", "55"].includes(str[0] + str[1]) &&
    str.length === 16
  ) {
    return "MasterCard";
  }
  return false;
}

console.log("Valid card:", checkCardValidity1("5121123498765431"));
console.log("Card types:", checkCardType("5121123498765431"));
