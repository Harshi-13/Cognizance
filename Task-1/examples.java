package project1;

import java.util.Scanner;

public class examples {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);    //System.in is a standard input stream  
		System.out.print("Enter first number- ");  
		int a= sc.nextInt();  
		System.out.print("Enter second number- ");  
		int b= sc.nextInt();  
		System.out.print("Enter third number- ");  
		int c= sc.nextInt();  
		int d=a+b+c;  
		System.out.println("Total= " +d);  
	}

}
