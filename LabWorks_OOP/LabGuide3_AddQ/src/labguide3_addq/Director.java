
package labguide3_addq;


public class Director {
    String name;
    int numberOfFilms;
    int oscars;
    String info;
    int earning;

    public Director() {
        name = "Alejandro González Iñárritu";
        numberOfFilms = 16;
        oscars = 7;
        info = " is well known movies like: Birdman, The Revenant";
    }

    public Director(String name, int numberOfFilms, int oscars, String info) {
        this.name = name;
        this.numberOfFilms = numberOfFilms;
        this.oscars = oscars;
        this.info = info;
    }
    
    public int earnings(){
        
        if ( (numberOfFilms / oscars)  < 5) {
            earning = 10000000;
            return earning;
        }
        else if( (numberOfFilms / oscars)  >= 5 && (numberOfFilms / oscars)  < 10){
            earning = 5000000;
            return earning;
        }
            
        
        else if( (numberOfFilms / oscars)  >= 10 && (numberOfFilms / oscars)  < 15)
        {
            earning = 1000000;
            return earning;
        }
            
        else{
            earning = 500000;
            return earning;
        }
            
    }

    public String getName() {
        return name;
    }

    public int getNumberOfFilms() {
        return numberOfFilms;
    }

    public int getOscars() {
        return oscars;
    }

    public String getInfo() {
        return info;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    
    public void display(){
        System.out.println("Director Information");
        System.out.println("-----------------------------");
        System.out.println("Name: " + name );
        System.out.println("Number Of Films: " + numberOfFilms);
        System.out.println("Oscar Wins and Nominees: " + oscars);
}
    
    public void display2(){
        System.out.println("\nDirector Information");
        System.out.println("-----------------------------");
        System.out.println("Name: " + name );
        System.out.println("Number Of Films: " + numberOfFilms);
        System.out.println("Oscar Wins and Nominees: " + oscars);
        System.out.println(info + ", earns " + earnings() + "$ per film");
        
    }
    
    
    
    
}
