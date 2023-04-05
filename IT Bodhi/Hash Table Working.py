"""
Hash :: Underlined data structure is Array
Key --> Hash Function  ==> This will generate an index (Deterministic)
Value --> is added to the index generated to the array
There could be possibility that at one index there would be multiple values. ==> Collision
Then convert this Linked List and keep it linear up-to threshold length else it will convert it into Balanced BST.
If the chaining is more, then Reloading of the Hash happens
Reload Hash
    - Load Factor --> L/N :: Tell us how much efficient is the hash.
    - it increases the indexes automatically and value copying happens and takes O(N) time.
"""