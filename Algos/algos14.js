/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
// You will need more parameters!
 function generateAnagrams(str, ana = [], pactual = "") {
    var str = []
    var ana = []
    var pactual = ""
    for (let i=0; i<str.length; i++){
    if (str[i] > ana){
        return str
    }
    if (str[i] == str[i] -1){
    elif
     }
    }

console.log(generateAnagrams(str1)) //["ilm", "iml", "lim", "lmi", "mil", "mli"] (order may vary, that's okay)