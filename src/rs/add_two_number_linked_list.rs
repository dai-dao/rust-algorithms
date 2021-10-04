use std::fmt;


#[derive(Debug, Clone)]
struct Node {
    val : i8,
    next : Option<Box<Node>>
}

impl Node {
    fn new(val : i8) -> Node {
        return Node { val : val, next : None }
    }
}

impl fmt::Display for Node {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Write strictly the first element into the supplied output
        // stream: `f`. Returns `fmt::Result` which indicates whether the
        // operation succeeded or failed. Note that `write!` uses syntax which
        // is very similar to `println!`.
        let mut outputs : Vec<String> = Vec::new();
        outputs.push(self.val.to_string());
        let mut next = &self.next;
        // as_ref borrows the reference content
        while next.is_some() {
            outputs.push(next.as_ref().unwrap().val.to_string());
            next = &next.as_ref().unwrap().next;
        }
        write!(f, "{}", outputs.join(""))
    }
}



struct Solution {}
impl Solution {

    fn add_recursive(l1: Node, l2: Node, c: i8) -> Node {
        let mut a = &mut l1.clone();
        let mut b = &mut l2.clone();
        let val = a.val + b.val + c;
        let mut ret = Node::new(val % 10);
        let new_c = val / 10;

        if a.next.is_some() || b.next.is_some() {
            if !a.next.is_some() {
                a.next = Some(Box::new(Node::new(0)));     
            }
            if !b.next.is_some() {
                b.next = Some(Box::new(Node::new(0)));     
            }
            ret.next = Some(Box::new(Solution::add_recursive(*a.next.as_ref().unwrap().clone(), 
                                                             *b.next.as_ref().unwrap().clone(), 
                                                             new_c)));
        } else if new_c > 0 {
            ret.next = Some(Box::new(Node::new(new_c)));
        }
        return ret;
    }

    fn add_iterative(l1: Node, l2: Node) -> Node {
        let mut a = Some(Box::new(l1));
        let mut b = Some(Box::new(l2));
        let mut c = 0;
        let mut ret = Node::new(0);
        let mut current = &mut Node::new(0);
        let mut first_node = true;

        while a.is_some() || b.is_some() {
            let val = a.as_ref().unwrap().val + b.as_ref().unwrap().val + c;
            c = val / 10;

            if first_node {
                ret = Node::new(val % 10);
                current = &mut ret;
                first_node = false;
            } else {
                current.next = Some(Box::new(Node::new(val % 10)));
                current = current.next.as_mut().unwrap();
            }
            //
            if a.as_ref().unwrap().next.is_some() || b.as_ref().unwrap().next.is_some() {
                if !a.as_ref().unwrap().next.is_some() {
                    a.as_mut().unwrap().next = Some(Box::new(Node::new(0)));
                }
                if !b.as_ref().unwrap().next.is_some() {
                    b.as_mut().unwrap().next = Some(Box::new(Node::new(0)));
                }
            } else if c > 0 {
                current.next = Some(Box::new(Node::new(c)));
            }
            // use clone to fix the value moved error
            a = a.as_ref().unwrap().next.clone();
            b = b.as_ref().unwrap().next.clone();
        }        

        return ret;
    }
}



pub fn solve() {
    let mut l1 : Node = Node::new(2);
    let mut l1_1 : Node = Node::new(4);
    l1_1.next = Some(Box::new(Node::new(3)));
    l1.next = Some(Box::new(l1_1));
    //
    let mut l2 : Node = Node::new(5);
    let mut l2_1 : Node = Node::new(6);
    l2_1.next = Some(Box::new(Node::new(4)));
    l2.next = Some(Box::new(l2_1));
    
    // clone because it's already moved
    println!("{} + {} = {}", l1, l2, Solution::add_iterative(l1.clone(), l2.clone()));
    println!("{} + {} = {}", l1, l2, Solution::add_recursive(l1.clone(), l2.clone(), 0));
}