# 0x13. JavaScript - Objects, Scopes and Closures

In this module, I learnt objects, `this` `undefined`, variable type and scope, closure, protype and inheritance.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by ALX School.

## Function Prototypes :floppy_disk:

Prototypes for some functions written in this project:

|File		     | Prototype				               |
| ------------------ | ------------------------------------------------------- |
| `7-occurrences.js` |`exports.nbOccurences = function (list, searchElement)`  |
| `8-esrever.js`     | `exports.esrever = function (list)`                     |
| `9-logme.js`       | `exports.logMe = function (item)`                       |
| `10-converter.js`  | `exports.converter = function (base)`                   |


## Tasks :page_with_curl:

* **0. Rectangle #0**
	* [0-rectangle.js](./0-rectangle.js): empty class `Rectangle` that defines a rectangle.

* **1. Rectangle #1**
	* [1-rectangle.js](./1-rectangle.js): class `Rectangle` that defines a rectangle. Updates [0-rectangle.js](./0-rectangle.js) by adding:
		* a constructor that takes 2 arguments `w` and `h`

* **2. Rectangle #2**
	* [2-rectangle.js](./2-rectangle.js): class `Rectangle` that defines a rectangle. Updates [1-rectangle.js](./1-rectangle.js):
		* If `w` or `h` is equal to `0` or not a positive integer, create an empty object.

* **3. Rectangle #3**
	* [3-rectangle.js](./3-rectangle.js): class `Rectangle` that defines a rectangle. Updates [2-rectangle.js](./2-rectangle.js):
		* an instance method called `print()` that prints the rectangle using the character `X`.

* **4. Rectangle #4**
	* [4-rectangle.js](./4-rectangle.js): a class Rectangle that defines a rectangle. Updates [3-rectangle.js](./3-rectangle.js):
		* an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
		* an instance method called `double()` that multiples the `width` and the `height` of the rectangle by `2`

* **5. Square #0**
	* [5-square.js](./5-square.js): a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
		* uses the class notation for defining class and `extends`
		* The constructor takes `1` argument: `size`

* **6. Square #1**
	* [6-square.js](./6-square.js): a class `Square` that defines a square and inherits from `Square` of `5-square.js`. Adds
		* an instance method called `charPrint(c)` that prints the rectangle using the character `c`
If c is undefined, use the character `X`.

* **7. Occurrences**
	* [7-occurrences.js](./7-occurrences.js): a function that returns the number of occurrences in a list:

* **8. Esrever**
	* [8-esrever.js](./8-esrever.js): a function that returns the reversed version of a list:


* **9. Log me**
	* [9-logme.js](./9-logme.js): a function that prints the number of arguments already printed and the new argument value.Output format: `<number arguments already printed>: <current argument value>`

* **10. Number conversion**
	* [10-converter.js](./10-converter.js): a function that converts a number from base 10 to another base passed as argument:

* **11. Factor index**
	* [100-map.js](./100-map.js): a script that imports an array and computes a new array.
		* script must import `list` from the file [100-data.js](./100-data.js).

* **12. Sorted occurences**
	* [101-sorted.js](./101-sorted.js): a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
		* script imports `dict` from the file [101-data.js](./101-data.js)
		* In the new dictionary:
			* A key is a number of occurrences
			* A value is the list of user ids
		* Prints the new dictionary at the end

* **13. Concat files**
	* [102-concat.js](./102-concat.js):  a script that concats `2` files.
		* The first argument is the file path of the first source file
		* The second argument is the file path of the second source file
		* The third argument is the file path of the destination
