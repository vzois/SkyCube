#include<iostream>

#include "../common/ArgParser.h"


void test_argparser(int argc, char **argv){
	ArgParser ap;

	ap.add_argument("-n",_INT,"128","Set cardinality");
	ap.add_argument("-d",_INT,"4","Set dimensionality");
	ap.add_argument("-distr",_STRING,"i","Set distribution");
	ap.parse_arguments(argc,argv);

	std::string distr = ap.get_string("-distr");
	uint32_t n = ap.get_int("-n");
	uint32_t d = ap.get_int("-d");

	std::cout<< "c:" << d << std::endl;
	std::cout<< "d:" << d << std::endl;
	std::cout<< "distr:" << distr << std::endl;
}

int main(int argc, char **argv){

	test_argparser(argc,argv);

	return 0;
}
