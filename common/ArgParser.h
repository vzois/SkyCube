#ifndef ARGP_H
#define ARGP_H

/*
 * @author Vasileios Zois
 * @email vzois@usc.edu
 *
 * Utility functions to parse command line arguments.
 */

#include <iostream>
#include <string>
#include <map>
#include <iomanip>
#include <vector>

enum Type{
	_STRING,
	_INT,
	_UINT,
	_BOOL,
	_FLOAT,
};

class ArgData{
	public:
		ArgData(Type type, std::string def, std::string help_msg){
			this->type = type;
			this->value = def;
			this->help_msg = help_msg;
		};

		~ArgData(){

		};

		void set_value(std::string value) {this->value = value;}
		std::string get_value() { return this->value; }
	private:
		Type type;
		std::string value;
		std::string help_msg;

};


class ArgParser{
	public:
		ArgParser(){};
		~ArgParser(){};

		void parseArgs(int argc, char **argv);
		void parse_arguments(int argc, char **argv);
		void add_argument(std::string identifier, Type type, std::string def_val, std::string help_msg);

		std::string get_string(std::string identifier){ exist_error(identifier); return this->_args[identifier]->get_value(); }
		int get_int(std::string identifier){ exist_error(identifier); return atoi(this->_args[identifier]->get_value().c_str()); }
		float get_float(std::string identifier){ exist_error(identifier); return atof(this->_args[identifier]->get_value().c_str()); }

		void menu();

	private:
		void init_error(std::vector<std::string> tokens,uint32_t i);
		void exist_error(std::string identifier);
		std::vector<std::string> split(std::string str, std::string delimiter);
		std::map<std::string,std::string>  args;
		std::map<std::string,ArgData*> _args;
};

std::vector<std::string> ArgParser::split(std::string str, std::string delimiter){
	std::vector<std::string> out;
	std::string lstr(str);
	int pos = 0;

	while ((pos = lstr.find(delimiter)) != -1){
		out.push_back(lstr.substr(0, pos));
		lstr = lstr.substr(pos + 1);
	}
	out.push_back(lstr);
	return out;
}

void ArgParser::parse_arguments(int argc, char **argv){
	for(int i = 1;i<argc;i++){
		std::vector<std::string> tokens = this->split(std::string(argv[i]),"=");
		this->init_error(tokens,i);
		this->exist_error(tokens[0]);
		this->_args[tokens[0]]->set_value(tokens[1]);
	}
}

void ArgParser::add_argument(std::string identifier, Type type, std::string def_val, std::string help_msg){
	this->_args.insert(std::pair<std::string,ArgData*>(identifier,new ArgData(type,def_val,help_msg)));
}

void ArgParser::menu(){

}

void ArgParser::init_error(std::vector<std::string> tokens, uint32_t i){
	if (tokens.size() < 2 || tokens[1] == "") {
		std::cout<< "Missing value for argument #"<< i << std::endl;
		exit(1);
	}
}

void ArgParser::exist_error(std::string identifier){
	if ( this->_args.find(identifier) == this->_args.end() ) {
		std::cout << "Unrecognized argument: " << identifier << std::endl;
		exit(1);
	}
}

#endif
