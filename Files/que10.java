package ass1;

import java.util.Scanner;

public class que10 {

	public static void main(String[] args) {

		Scanner qwe = new Scanner(System.in);
		System.out.println("to calculate m^n");
		System.out.println("enter value of m: ");
		int m = qwe.nextInt();
		System.out.println("enter value of n: ");
		int n = qwe.nextInt();
		int pow = 1;
		for (int i=1; i<n+1; i++)
			pow = m*pow;
		System.out.println(pow);
		qwe.close();

	}

}
