
#[derive(Debug)]
struct Node {
    value : i8,
    // recrusive so using Box to make reference instead, Option because it could be null
    left: Option<Box<Node>>,
    right: Option<Box<Node>>
}

impl Node {
    // indicates the data pointed to by the reference lives for the entire lifetime of 
    // the running program
    pub fn new(val: i8) -> Self {
        return Node { value : val, left : None, right : None };
    }
}


struct Solution;
impl Solution {

    fn _is_valid_bst_helper(node: Option<Box<Node>>, low : i8, high : i8) -> bool {
        if let Some(node_box) = node {
            if node_box.value > low && node_box.value < high &&
                Solution::_is_valid_bst_helper(node_box.left, low, node_box.value) &&
                Solution::_is_valid_bst_helper(node_box.right, node_box.value, high)
            {
                return true;
            } else {
                return false;
            }
        } else {
            return true;
        }
    }

    fn is_valid_bst(node : Node) -> bool {
        return Solution::_is_valid_bst_helper(Some(Box::new(node)), -100, 100);
    }
}


pub fn solve() {
    let mut root = Node::new(5);
    root.left = Some(Box::new(Node::new(4)));
    root.right = Some(Box::new(Node::new(7)));
    println!("Out {}",  Solution::is_valid_bst(root));
    // should build the tree bottom-up
    let mut root2 = Node::new(5);
    root2.left = Some(Box::new(Node::new(4)));
    let leaf = Node::new(2);
    let mut right_node = Node::new(7);
    right_node.left = Some(Box::new(leaf));
    root2.right = Some(Box::new(right_node));
    println!("Out {}",  Solution::is_valid_bst(root2));
}