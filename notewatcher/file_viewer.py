import os
from cominfer import PythonFunctionFinder


class FileViewer(PythonFunctionFinder):
    def view_file(self, file_path):
        view_function = self._get_view_function(file_path)
        view_function(file_path)

    def _get_view_function(self, file_path):
        view_function_name = self._view_function_name_for_file(file_path)
        view_function = self._find_view_functions().get(view_function_name)
        if not view_function:
            raise FileNotFoundError(f"Didn't find a function named {view_function_name} in viewdir")
        return view_function

    def _find_view_functions(self):
        return {
            name: function
            for name, function in self.find_functions().items()
            if name.startswith('view_')
        }
    
    @staticmethod
    def _view_function_name_for_file(file_path):
        file_ext = os.path.splitext(file_path)[1][1:]
        return f"view_{file_ext}"