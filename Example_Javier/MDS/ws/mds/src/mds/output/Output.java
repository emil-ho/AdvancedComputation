
package mds.output;

import java.awt.*;
import mds.common.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;
public class Output implements mds.common.IOutput {
  /**
   * 
   * The experiment object, with (almost) all information to generate output, with particles positions
   * and with all constants necesary to convert units.
   * 
   */
  private mds.common.InputData experiment;

  /**
   * 
   * The results files object, whose names are taken, edited (with the extension), and then returned.
   * 
   */
  private mds.common.ResultsFiles resultsFiles;

  /**
   * 
   * The object of the inner class resultFiles. To be created only once, and used by all private methods.
   * 
   */
  private Output.OutputTextFiles files;

  /**
   * This static method returns an OutputModule object that implements the interface IOutput.
   * It does nothing else, as experiment data is not given yet.
   * 
   * @return an object that implements the interface IOutput
   */
  public static mds.common.IOutput createOutput()
  {
return new Output();
  }

  /**
   * This makes the results for the experiment, making the text files and the plots. The names
   * of all the files are written in the resultFiles object (overwritng it).
   * 	@param experiment Is the experiment object with the data needed to retrive
   * the simulation results (without the extensions).
   * 	@return returns The ResultsFile object with the names of all the requested 
   * resulting images and data files generated. If any of those files could not 
   * be generated the corresponding string would be a null reference. This includes the
   * extensions of each file. Also, this is the same as the resultFiles given object.
   */
  public ResultsFiles results(mds.common.InputData experiment, mds.common.ResultsFiles resultsFiles) {
	return null;
  }

  /**
   * This creates the output object (but does nothing else).
   */
  public Output() {
  }

  /**
   * This creates the energy plot (with the kinetic energy, the potential energy and the total
   * one as function of the step number). It gives the image and a text file with data. The names
   * of the files are writen in files, the object from ResultsFiles.
   */
  private void energyPlot() {
  }

  /**
   * This method generates the output for the initial velocity histogram. It both generates an
   * image and a text file, and register it's names in files, from resultsFiles object.
   */
  private void velocityPlot() {
  }

  /**
   * This generates a pair distribution function plot. It both represents it in an image and
   * writes the data in a text file. Then, the names of those files are included in files, the
   * object of ResultsFiles.
   */
  private void pairDistributionPlot() {
  }

  protected class OutputTextFiles {
    /**
     * The constructor. Initialization of general features can be done here.
     */
    public OutputTextFiles() {
 
    }

    /**
     * Method that makes a .txt file with the velocity (in its units) with the frecuency 
     * of each one.
     * This .txt file contains 2 columns, one with the velocities and another with the 
     * frecuencies.
     * 	@param velocityData A 2 dimensional array. The first cordinate can be 0
     * 	(for the x points, velocities) or 1 (for the y points, frequency of them). 
     * 	The second index refeers to each point. 
     */
    public void velocityTextFile(double[][] velocityData) {
 
    }

    /**
     * Method that makes a .txt file with the distance between 2 particles 'r' (in its units),
     * the value of the pair distribution function in that point and the value of the potential
     * in the same 'r'.
     * This .txt file contains 3 columns, one with the values of 'r', another with the
     * values of the pair distribution function 'G(r)', and another with the values of the
     * potential 'V(r)'.
     * 	@param pairDistributionData A 3 dimensional array. The first cordinate can be 0 
     * 	(for the x points, the distances), 1 (for the y points, the values of 'G(r)'),
     * 	or 2 (for the y points, the values of 'V(r)').
     * 	 The second index refeers to each point. 
     */
    public void pairDistributionTextFile(double[][] pairDistributionData) {
 
    }

    /**
     * Method that makes a .txt file with the steps and with the potential, kinetic and total
     * energy (in its units).
     * This .txt file contains 4 columns, one with the steps, another with the values of the 
     * potential energies, another with the values of the kinetic energies and the last one
     * with the values of the total energy.
     * 	@param velocityData A 4 dimensional array. The first cordinate can be 0
     * 	(for the x points, the step), 1 (for the y points, the potential energy),
     * 	2 (for the y points, the kinetic energy) or 3 (for the y points,
     * 	the total energy). 
     * 	The second index refeers to is point. 
     */
    public void energyTextFile(double [][] energyData) {
 
    }

  }

  protected class OutputMovies {
    /**
     * This converts the internal units to Amstrong (for the output in XCryDen).
     */
    private double lengthConverterA;

    /**
     * The factor to convert the velotity units from internal to the ones of the movies.
     */
    private double velocityConverterA;

    /**
     * The factor to convert the force (or acelerations) units from internal to the ones of the movies.
     */
    private double forceConverterA;

    /**
     * This is the number of steps the movie will have.
     */
    private int nSteps = experiment.movie.size();

    /**
     * This is the number of atoms the unit cell has. It depends on the kind (FCC or BCC).
     */
    private int nPartCell;

    /**
     * The constructor for OutputMovies, where some features are intitalized (unit conversion...)
     */
    public OutputMovies() {
 
    }

    /**
     * This creates a movie with the particle's positions. It exports a text file which, latter on,
     * can be read by xCryDen program (externaly). The name of the file is included in files, the
     * objet from ResultsFiles.
     */
    public void positionMovie() {
 
    }

    /**
     * This creates a velocity movie, with the particle's positions and the velocities represented
     * as arrows. It exports a text file which, latter on, can be read by xCryDen program
     * (externaly). The name of the files are included in files, object from ResultsFiles.
     */
    public void velocityMovie() {
 
    }

    /**
     * This creates a velocity movie, with the particle's positions and the forces (proportional
     * to acelerations) represented as arrows. It exports a text file which, latter on, 
     * can be read by xCryDen program (externaly). The name is written in files,
     * from ResultsFiles.
     */
    public void forceMovie() {
 
    }

  }

}
