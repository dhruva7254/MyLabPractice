package ass1;

import java.util.*;

public class que5 {

	public static void main(String[] args) {
		
		Scanner qwe = new Scanner(System.in);
		System.out.println("enter the number: ");
		int a = qwe.nextInt();
		if (a%5 == 0)
			if (a%7 == 0)
				System.out.println("divisible by 5 and 7");
			else
				System.out.println("not divisible by 5 and 7");
		else
			System.out.println("not divisible by 5 and 7");
		qwe.close();
			
	}

}
