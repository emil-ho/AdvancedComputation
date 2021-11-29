
package mds.common;

/**
 * This interface extends the ILongSimulationManager interface by adding the method that invokes an actual simulation.
 */
public interface IMDS extends ILongSimulationManager {
  /**
   * Runs a simulation of the given experiment up to completion and produces 
   * the output results. 
   * 
   * @param experiment is the experiment object with the data needed to configure and 
   * run the simulation
   * @return returns the ResultsFile object with the names of all the requested 
   * resulting images and data files generated. If any of those files could not 
   * be generated the corresponding string would be a null reference.
   */
  ResultsFiles simulate(InputData experiment) ;

}
