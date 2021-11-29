
package mds.common;

public class ResultsFiles {
  /**
   * Name of the .png, .jpg or .bmp image of the initial velocities distribution histogram.
   */
  public String velocitiesHistogramImage;

  /**
   * Name of the text file with the initial velocities distribution histogram data
   */
  public String velocitiesHistogramData;

  /**
   * Name of the .png, .jpg or .bmp image of the pair distribution function, including also the potential (this is a supplot). 
   */
  public String potentialAndPairDistributionFunctionImage;

  /**
   * Name of the .png, .jpg or .bmp image of the potencial, as function of the distance between particles.
   */
  public String potentialImage;

  /**
   * Name of the .png, .jpg or .bmp image of the pair distribution function.
   */
  public String pairDistributionFunctionImage;

  /**
   * Name of the text file with the potential and the pair distribution function listed together
   */
  public String potentialAndPairDistFunctionData;

  /**
   * Name of the .png, .jpg or .bmp image of the potential, kineitc and total energies plotted in the same graph.
   */
  public String energyImage;

  /**
   * Name of the text fle with the potential, kineitc and total energies listed for all the steps of the simulation.
   */
  public String energyData;

  /**
   * This constains the name of the text file to be read by xCryDen to generate the position movie.
   */
  public String positionMovieData;

  /**
   * This constains the name of the text file to be read by xCryDen to generate the velocity movie.
   */
  public String velocityMovieData;

  /**
   * This constains the name of the text file to be read by xCryDen to generate the velocity movie.
   */
  public String forceMovieData;

  /**
   * This constructor makes the ResultsFiles, and saves it's names using the given prefix and suffix.
   * The extensions (.txt, .jpg ...) are not included yet.
   * 	@param prefix This is the name of the directory (absolute), and includes the last "\" symbol for the folder, as a string.
   * 	@param suffix The name to be added to each file (experiment name). Do not include any special character.
   */
  public ResultsFiles(String prefix, String suffix) {
/*
 * The names of the files are composed of the prefix, a name specifying what it is (that is included here).
 */
velocitiesHistogramImage = prefix + "velocitiesHistogramImage_" + suffix;
velocitiesHistogramData  = prefix + "velocitiesHistogramData_" + suffix;
potentialAndPairDistributionFunctionImage = prefix + "potentialAndPairDistributionFunctionImage_" + suffix;
potentialImage = prefix + "potentialImage_" + suffix;
pairDistributionFunctionImage = prefix + "pairDistributionFunctionImage_" + suffix;
potentialAndPairDistFunctionData = prefix + "potentialAndPairDistFunctionData_" + suffix;
energyImage = prefix + "energyImage_" + suffix;
energyData = prefix + "energyData_" + suffix;
positionMovieData = prefix + "positionMovieData_" + suffix;
velocityMovieData = prefix + "velocityMovieData_" + suffix;
forceMovieData= prefix + "forceMovieData_" + suffix;
  }

}
