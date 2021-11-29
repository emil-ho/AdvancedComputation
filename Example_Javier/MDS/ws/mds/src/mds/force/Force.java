
package mds.force;

import mds.common.*;
/**
 * This class calculates the current accelerations for all particles.
 */
public class Force implements mds.common.IForce {
  /**
   * The state for which forces and hence accelerations are calculated.
   * This value is initialized by the constructor.
   */
  protected mds.common.State s;

  /**
   * This static method creates an object of a class that implements the IForce interface
   * 
   * @param s the reference to the state object that holds the system for which the 
   * acceleration and potentials will be calculated.
   * @return an object of a class that implements the IForce interface
   */
  public static mds.common.IForce createForce(mds.common.State s)
  {
    	  return new Force(s);
  }

  /**
   * This constructor receives the state for which the Force object
   * will be created.
   * 
   * @param s the state for whose particles the accelerations will be 
   * calculated when requested
   */
  public  Force(mds.common.State s) {
      this.s = s;
  }

  /**
   * Calculates the forces that apply to all particles and update the 
   * corresponding accelerations in the current State. The operation 
   * returns the current potential energy of the system. 
   * The positions of every particle are taken from State, as well as the 
   * neighbour list of each particle. For a particle, just the particles 
   * stated in the neighbour list are taken into account.
   * The force acting over a particle because of the other ones has three components. 
   * First, it calculates the distance between each neighbour particle and 
   * the force is calculated using the equation for every particle against this one,
   * therefore the total force in a component is the sum of all these pair forces.
   * The force acting on a particle operates in the same way for the 3 components.
   * 
   * @return a double real value with the current potential energy of the system.
   */
  public double calcForce() {
    	//TODO...?
    
    	return 0.0;
  }

  /**
   * This function returrns the potential between two particles of the 
   * current experiment evaluated for a concrete distance given as input
   * parameter.
   * 
   * @param distance value in meters that indicates the distance between 
   * the particles for which the potential is to be calculated
   * @return value of the potential calculated for two particles of the current 
   * experiment when they are at the distance given as invocation argument.  
   */
  public double evalPotential(double distance) {
    	//TODO...?
    
    	return 0.0;
  }

  /**
   * This method returns a graph in the form of a list of points (x,y) that 
   * describes the potential for the range of distance values observed in the 
   * current experiment.
   * The number of points is taken from the method numberOfPoints that comes from Input.
   * The objective of this method is to provide (review) graph which contains two list of numbers
   * In the x coordinate we take as a first value, the minimum distance mind and as a maximum
   * value the maximum distance maxd. The intermediate points are values separate (maxd-mind)/numberOfPoints
   * In the Y coordinate, the potential for each value of the distances is calculated using the method evalPotential
   * 
   * @return a graph that is a list of pairs of numbers (x,y). These values 
   * are of the type double. x represents the distance in meters and y potentials
   * in energy units. The first and last points in the graph correspond to the minimum and 
   * maximum distances observed among all particles in the current experiment.
   */
  public mds.common.Graph drawPotential() {
    	//TODO...!
    
    	return null;
  }

  /**
   * This method takes from the class Force maxd and mind from the current state.
   * It will divide the interval between mind and maxd in some divisions which 
   * are collected in X. It will calculate the number of particles in each division
   * and collect these values on the Y axis.
   */
  public mds.common.Graph drawPairDistributionFunction() {
    	//TODO...!
    
    	return null;
  }

}
