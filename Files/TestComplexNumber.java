package tester;
import day3practice1.ComplexNumber;
import java.util.Scanner;
public class TestComplexNumber 
{
	public static void main(String[] args) 
	{
		Scanner qwe = new Scanner(System.in);
		System.out.println("enter the real & imaginary part: ");
		float a = qwe.nextFloat();
		float b = qwe.nextFloat();
		ComplexNumber comnumobj1 = new ComplexNumber();
		comnumobj1.assignComplexNumber(a, b);
		comnumobj1.showComplexNumber();
		qwe.close();
	}
}