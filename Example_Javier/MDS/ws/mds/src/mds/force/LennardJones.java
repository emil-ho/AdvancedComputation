
package mds.force;

import mds.common.*;
/**
 * This class uses the LennarJones potential to calculate the current accelerations 
 * for all particles.
 */
class LennardJones extends Force {
  /**
   * This constructor receives the state for which the Force object
   * will be created. This class uses the LennarJones potential.
   * 
   * @param s the state for whose particles the accelerations will be 
   * calculated when requested
   */
  public  LennardJones(mds.common.State s) {
      super(s);
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
	//TODO...!

	return 0.0;
  }

  /**
   * This function returns the potential between two particles of the 
   * current experiment evaluated for a concrete distance given as input
   * parameter.
   * 
   * @param distance value in meters that indicates the distance between 
   * the particles for which the potential is to be calculated
   * @return value of the potential calculated for two particles of the current 
   * experiment when they are at the distance given as invocation argument.  
   */
  public double evalPotential(double distance) {
	//TODO...!

	return 0.0;
  }

}
