use std::collections::HashMap;



pub struct Solution {}

impl Solution {

    fn can_spell(magazine : Vec<char>, note : String) -> bool {
        let mut map : HashMap<char, i8> = HashMap::new();
        
        for c in magazine.iter() {
            let value = map.get(c).cloned().unwrap_or(0);
            map.insert(*c, value+1);
        }

        for c in note.chars() {
            let value = map.get(&c).cloned().unwrap_or(0);
            if value <= 0 {
                return false
            }
            map.insert(c, value - 1);
        }

        return true
    }
}


pub fn solve() {
    println!("{}", Solution::can_spell(vec!{'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g'}, "bed".to_owned()));
    println!("{}", Solution::can_spell(vec!{'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g'}, "beaad".to_owned()));
    println!("{}", Solution::can_spell(vec!{'a', 'b', 'c', 'd', 'e', 'f', 'g'}, "cat".to_owned()));
}