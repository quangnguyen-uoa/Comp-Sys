string VMTranslator::vm_function(string function_name, int n_vars){
    string translator="";
    translator=translator+"("+function_name+")\n";
    for (int i=0; i<n_vars; i++) {
        translator=translator+"@SP\nA=M\nM=0\n@SP\nM=M+1\n";
    }
    return translator;
}