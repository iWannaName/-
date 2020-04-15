import java.util.ArrayList;
import java.util.Iterator;

public class ListRemove {
	public static void main(String[] args) {
	ArrayList<Integer> list = new ArrayList<>();
	list.add(1);
	list.add(1);
	list.add(2);
	list.add(2);
	list.add(3);
	System.out.println(list);
	Iterator<Integer> it=list.iterator();
	while(it.hasNext()) {
		int i=it.next();
		if(i==1) {
			it.remove();
		}
		
		System.out.println(list);
	}
			
	}
}
