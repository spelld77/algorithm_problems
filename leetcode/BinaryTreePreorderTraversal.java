import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class  BinaryTreePreorderTraversal {

	public static void main(String[] args) {

		
		TreeNodes obj5= new TreeNodes(12, null, null);
		TreeNodes obj3= new TreeNodes(5, null, null);
		TreeNodes obj2= new TreeNodes(9, obj3, obj5);
		TreeNodes obj4= new TreeNodes(7, null, null);
		TreeNodes obj1= new TreeNodes(3, obj2, obj4);
		
		BinaryTreePreorderTraversal tem = new BinaryTreePreorderTraversal();
		System.out.println(tem.preorderTraversal(obj1));
	}
	
	public List<Integer> preorderTraversal(TreeNodes root) {
		
		List<Integer> list = new ArrayList<Integer>();
		if(root == null) return list;
		
		Stack<TreeNodes> stack = new Stack<>();
		stack.push(root);
		
		while(!stack.isEmpty()) {
			TreeNodes node = stack.pop();
			list.add(node.val);
			
			if(null != node.left) {
				list.addAll(preorderTraversal(node.left));
			}
			if(null != node.right) {
				list.addAll(preorderTraversal(node.right));
			}
		}
		
		return list;
	}
	
	

}

class TreeNodes{
	int val;
	TreeNodes left;
	TreeNodes right;
	
	public TreeNodes(int val) {
		this.val = val;
	}
	public TreeNodes(int val, TreeNodes left, TreeNodes right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}
