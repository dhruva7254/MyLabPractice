package ass1;

import java.util.*;

public class que9 {
	
//	public int fac(int num)
//	{
//		int fact = 
//		return fact;
//	}

	public static void main(String[] args) {

//		Scanner qwe = new Scanner(System.in);
//		System.out.println("enter the number: ");
//		int a = qwe.nextInt();
//		int fact = 1;
//		int fact_1 = 1;
//		int sum=0;
//		//while (a>0)
//		for (int i=1; i<a+1; i--)
//			sum = i*(i-1);
//			fact += sum;
//		if (a == 0 | a == 1)
//			System.out.println(fact_1);
//		else
//			System.out.println(fact);
//			
//		qwe.close();
		
//		int n=5;
//		int fact=1;
//		int sum=0;
//		for (int i=n; i>1; i--)
//			fact = i*(i-1);
//			System.out.println(fact);
//			sum += fact;
//		System.out.println(sum);
		
//		int n=5;
//		int fac=1,asd=0;
//		for (int i=1; i<n; i++)
//			//System.out.println(i);
//			fac = 2*fac;
//			System.out.println(fac);
//			asd = asd + fac;
//		System.out.println(asd);
		
		Scanner qwe = new Scanner(System.in);
		System.out.println("enter the number: ");
		int a = qwe.nextInt();
		int fact = 1;
		for (int i=1; i<a;i++)
			fact=i*fact;
		System.out.println(fact);
		qwe.close();
		
	}

}
