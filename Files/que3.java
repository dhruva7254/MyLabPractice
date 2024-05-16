package ass1;

import java.util.Scanner;

public class que3 {

	public static void main(String[] args) {
		
		int a=0,b=0,c=0;
		System.out.println("enter two numbers: ");
		Scanner qwe = new Scanner(System.in);
		a=qwe.nextInt();
		b=qwe.nextInt();
		c=a;
		a=b;
		b=c;
		System.out.print(a+" "+b);
		qwe.close();
	}
}
