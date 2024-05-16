package ass1;

import java.util.*;

public class que7 {

	public static void main(String[] args) {

		Scanner qwe = new Scanner(System.in);
		System.out.println("enter a character: ");
		char a = qwe.next().charAt(0);
		//System.out.println(a);
		if (a == 'a' | a == 'e' | a == 'i' | a == 'o' | a == 'u')
			System.out.println("vowel");
		else
			System.out.println("consonant");
		qwe.close();

	}

}
