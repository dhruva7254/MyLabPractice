package ass1;

import java.util.*;

public class que6 {

	public static void main(String[] args) {
		
		Scanner qwe = new Scanner(System.in);
		System.out.println("enter the annual basic salary: ");
		double abs = qwe.nextInt();
		double tax = 0;
		if (abs<150000)
			tax = 0;
		if (abs>150000)
			if (abs<300000)
				tax = 0.20*abs;
			else 
				tax = 0.30*abs;
		System.out.println("Income Tax: "+tax);
		qwe.close();
		
	}

}
