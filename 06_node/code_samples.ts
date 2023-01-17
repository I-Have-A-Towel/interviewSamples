const myArr: number[] = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7];

/**
 * Q1: How would you keep only unique values from the array myArr
 */

// write answer here

/**
 * Q2: What is the difference between the 4 loops (forEach vs map vs for..in vs for..of) and their results?
 * What is:
 *  - value of `a`
 *  - value of `myList` after a is set
 *  - value of `b`
 *  - value of `myList` after b is set
 *  - value of `myList` after for..in loop
 *  - value of `myList` after for..of loop
 */

// MAP
let myList: number[];
myList = [1, 2, 3, 4, 5];
const a = myList.map(n => n * 2);

// FOR-EACH
myList = [1, 2, 3, 4, 5];
const b = myList.forEach(n => (n *= 2));

// FOR..IN
myList = [1, 2, 3, 4, 5];
for (let i in myList) {
  myList[i] *= 2;
}

// FOR..OF
myList = [1, 2, 3, 4, 5];
for (let n of myList) {
  n *= 2;
}

/**
 * Q3: How would you ensure that the 2nd element in array `myList` does NOT
 * get included in the resulting arrays `c` and `d`?
 */

myList = [1, 2, 3, 4, 5];
const c = myList.map(n => n * 2);

myList = [1, 2, 3, 4, 5];
let d = myList;
for (let i in d) {
  d[i] *= 2;
}

/**
 * Q4: Write a simple, typed promise function and use it in Promise.all.
 */
