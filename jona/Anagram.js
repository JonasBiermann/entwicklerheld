export function isAnagram(firstWord, secondWord) {
  if (firstWord.split("").sort().join() == secondWord.split("").sort().join()) {
    return true;
  } else {
    return false;
  }
}
