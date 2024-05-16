package ass1;

import java.util.*;

public class que8 {

	public static void main(String[] args) {

		Scanner qwe = new Scanner(System.in);
		System.out.println("enter the angles of a triangle: ");
		int a = qwe.nextInt();
		int b = qwe.nextInt();
		int c = qwe.nextInt();
		if (a+b+c == 180)
			System.out.println("valid triangle");
		else
			System.out.println("not a valid triangle");
		qwe.close();

	}

}
