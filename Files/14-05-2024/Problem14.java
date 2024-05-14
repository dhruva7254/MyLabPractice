
// 14: Write a  program to find sum of all even and odd numbers between 1 to n. 

package ass1;
import java.util.Scanner;
public class Problem14 {
	public static void main(String[] args) {
		Scanner qwe = new Scanner(System.in);
		System.out.print("enter value of n: ");
		int a = qwe.nextInt();
		System.out.println(a);
		int sume = 0,sumo = 0;
		for (int i=1; i<=a; i++)
			if (i%2 == 0)
				sume += i;
			else
				sumo += i;
		System.out.println("sum of all even numbers: "+sume);
		System.out.println("Sum of all odd numbers: "+sumo);
		qwe.close();
	}
}
