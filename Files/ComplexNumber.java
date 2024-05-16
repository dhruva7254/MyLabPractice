package day3practice1;
public class ComplexNumber 
{
	private float real;
	private float imaginary;
	public void assignComplexNumber(float r, float i)
	{
		real = r;
		imaginary = i;
	}
	public void showComplexNumber()
	{
		System.out.println("Real = "+real+" imaginary = "+imaginary);;
	}
}