
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARREGLO ARROBA BEGIN BOOLEANO BREAK CASE CLASS COMA COMILLASDOBLE COMILLASIMPLE COMPARACION DARROBA DEF DIVIDE DO DOLAR ELSE ELSIF END ENSURE FALSE FICHERO FOR GUIONBAJO HASH ID IF IGUAL LBRACKET LLLAVE LPAREN MINUS MODULE NEXT NIL NOT NUMBER OR PLUS PUNTO RBRACKET REDO RESCUE RETRY RETURN RLLAVE RPAREN SELF STRING SUPER THEN TIMES TRUE UNDEF UNLES UNTIL VARIABLE WHEN WHILE YIELDsentencias : estructurasControl\n                | declaracion\n                estructurasControl : estrucIf\n                            | estrucElse\n                            | estrucWhile\n                            operadorMat : IGUAL\n                | PLUS\n                | MINUS\n                | TIMES\n                operadorLog : AND\n                 | OR\n                estrucIf : IF logica cuerpo END\n                | IF logica cuerpo estrucElse\n                logica : condicion\n                | condicion operadorLog  logica\n                condicion : comparador COMPARACION comparador\n                    | boolean\n                    comparador : VARIABLE\n                    | primitivo\n                    estrucElse : ELSE cuerpo END\n                    | ELSE logica cuerpo END\n                     estrucWhile : WHILE logica cuerpo END\n                    cuerpo : declaracion\n                | declaracion cuerpo\n                | cuerpo RETURN retornos\n                retornos : VARIABLE\n                | primitivo\n                | expresion\n                | asignacion\n                declaracion : VARIABLE IGUAL asignacion\n                    | VARIABLE IGUAL asignacion declaracion\n                    | VARIABLE operadorMat IGUAL opcion\n                    | VARIABLE operadorMat IGUAL opcion declaracion\n                    opcion : VARIABLE\n                | NUMBER\n                declaracion : DEF VARIABLE LPAREN params RPAREN cuerpo ENDparams : rubyParams\n               | rubyParams COMA params\n                  rubyParams : VARIABLE\n                    | boolean\n                    | NUMBERasignacion : primitivoasignacion : HASHasignacion : ARREGLOasignacion : FICHEROasignacion : expresionasignacion : STRINGexpresion : NUMBER PLUS NUMBERexpresion : NUMBER MINUS NUMBERexpresion : terminotermino : termino TIMES factortermino : termino DIVIDE factortermino : factorfactor : NUMBERfactor : LPAREN expresion RPARENprimitivo : NUMBER PUNTO NUMBERprimitivo : NUMBERprimitivo : booleanboolean : TRUE\n             | FALSE\n        '
    
_lr_action_items = {'VARIABLE':([0,8,9,10,11,18,19,21,22,23,24,25,26,28,29,31,32,33,34,35,36,37,38,39,40,41,42,44,45,47,48,49,50,53,57,64,65,66,74,75,76,84,85,86,87,88,89,90,91,92,95,],[7,17,22,30,22,7,-14,-17,-18,-19,-59,-60,-57,7,7,7,7,-42,-43,-44,-45,-46,-47,-54,-58,-50,-53,64,67,22,-10,-11,22,78,-31,-34,7,-35,-15,-16,-56,-48,-49,-51,-54,-52,-55,-33,7,67,-36,]),'DEF':([0,10,18,19,21,22,23,24,25,26,28,29,31,32,33,34,35,36,37,38,39,40,41,42,57,64,65,66,74,75,76,84,85,86,87,88,89,90,91,95,],[8,8,8,-14,-17,-18,-19,-59,-60,-57,8,8,8,8,-42,-43,-44,-45,-46,-47,-54,-58,-50,-53,-31,-34,8,-35,-15,-16,-56,-48,-49,-51,-54,-52,-55,-33,8,-36,]),'IF':([0,],[9,]),'ELSE':([0,24,25,29,32,33,34,35,36,37,38,39,40,41,42,46,55,57,64,65,66,76,77,78,79,80,81,84,85,86,87,88,89,90,95,],[10,-59,-60,-23,-30,-42,-43,-44,-45,-46,-47,-54,-58,-50,-53,10,-24,-31,-34,-32,-35,-56,-25,-26,-27,-28,-29,-48,-49,-51,-54,-52,-55,-33,-36,]),'WHILE':([0,],[11,]),'$end':([1,2,3,4,5,6,24,25,32,33,34,35,36,37,38,39,40,41,42,52,57,64,65,66,72,73,76,82,83,84,85,86,87,88,89,90,95,],[0,-1,-2,-3,-4,-5,-59,-60,-30,-42,-43,-44,-45,-46,-47,-54,-58,-50,-53,-20,-31,-34,-32,-35,-12,-13,-56,-21,-22,-48,-49,-51,-54,-52,-55,-33,-36,]),'IGUAL':([7,12,13,14,15,16,30,],[12,-6,44,-7,-8,-9,12,]),'PLUS':([7,30,39,63,],[14,14,58,58,]),'MINUS':([7,30,39,63,],[15,15,59,59,]),'TIMES':([7,30,39,41,42,63,86,87,88,89,],[16,16,-54,60,-53,-54,-51,-54,-52,-55,]),'TRUE':([9,10,11,12,45,47,48,49,50,53,92,],[24,24,24,24,24,24,-10,-11,24,24,24,]),'FALSE':([9,10,11,12,45,47,48,49,50,53,92,],[25,25,25,25,25,25,-10,-11,25,25,25,]),'NUMBER':([9,10,11,12,43,44,45,47,48,49,50,51,53,58,59,60,61,92,],[26,26,26,39,63,66,71,26,-10,-11,26,76,39,84,85,87,87,71,]),'HASH':([12,53,],[34,34,]),'ARREGLO':([12,53,],[35,35,]),'FICHERO':([12,53,],[36,36,]),'STRING':([12,53,],[38,38,]),'LPAREN':([12,17,43,53,60,61,],[43,45,43,43,43,43,]),'AND':([19,21,22,23,24,25,26,40,75,76,],[48,-17,-18,-19,-59,-60,-57,-58,-16,-56,]),'OR':([19,21,22,23,24,25,26,40,75,76,],[49,-17,-18,-19,-59,-60,-57,-58,-16,-56,]),'COMPARACION':([20,21,22,23,24,25,26,30,76,],[50,-58,-18,-19,-59,-60,-57,-18,-56,]),'END':([24,25,27,29,32,33,34,35,36,37,38,39,40,41,42,46,54,55,56,57,64,65,66,76,77,78,79,80,81,84,85,86,87,88,89,90,93,95,],[-59,-60,52,-23,-30,-42,-43,-44,-45,-46,-47,-54,-58,-50,-53,72,82,-24,83,-31,-34,-32,-35,-56,-25,-26,-27,-28,-29,-48,-49,-51,-54,-52,-55,-33,95,-36,]),'RETURN':([24,25,27,29,32,33,34,35,36,37,38,39,40,41,42,46,54,55,56,57,64,65,66,76,77,78,79,80,81,84,85,86,87,88,89,90,93,95,],[-59,-60,53,-23,-30,-42,-43,-44,-45,-46,-47,-54,-58,-50,-53,53,53,53,53,-31,-34,-32,-35,-56,-25,-26,-27,-28,-29,-48,-49,-51,-54,-52,-55,-33,53,-36,]),'COMA':([24,25,67,69,70,71,],[-59,-60,-39,92,-40,-41,]),'RPAREN':([24,25,41,42,62,63,67,68,69,70,71,84,85,86,87,88,89,94,],[-59,-60,-50,-53,89,-54,-39,91,-37,-40,-41,-48,-49,-51,-54,-52,-55,-38,]),'PUNTO':([26,39,],[51,51,]),'DIVIDE':([39,41,42,63,86,87,88,89,],[-54,61,-53,-54,-51,-54,-52,-55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'estructurasControl':([0,],[2,]),'declaracion':([0,10,18,28,29,31,32,65,91,],[3,29,29,29,29,29,57,90,29,]),'estrucIf':([0,],[4,]),'estrucElse':([0,46,],[5,73,]),'estrucWhile':([0,],[6,]),'operadorMat':([7,30,],[13,13,]),'logica':([9,10,11,47,],[18,28,31,74,]),'condicion':([9,10,11,47,],[19,19,19,19,]),'comparador':([9,10,11,47,50,],[20,20,20,20,75,]),'boolean':([9,10,11,12,45,47,50,53,92,],[21,21,21,40,70,21,40,40,70,]),'primitivo':([9,10,11,12,47,50,53,],[23,23,23,33,23,23,79,]),'cuerpo':([10,18,28,29,31,91,],[27,46,54,55,56,93,]),'asignacion':([12,53,],[32,81,]),'expresion':([12,43,53,],[37,62,80,]),'termino':([12,43,53,],[41,41,41,]),'factor':([12,43,53,60,61,],[42,42,42,86,88,]),'operadorLog':([19,],[47,]),'opcion':([44,],[65,]),'params':([45,92,],[68,94,]),'rubyParams':([45,92,],[69,69,]),'retornos':([53,],[77,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> estructurasControl','sentencias',1,'p_sentecias','sintactico.py',7),
  ('sentencias -> declaracion','sentencias',1,'p_sentecias','sintactico.py',8),
  ('estructurasControl -> estrucIf','estructurasControl',1,'p_estructurasControl','sintactico.py',14),
  ('estructurasControl -> estrucElse','estructurasControl',1,'p_estructurasControl','sintactico.py',15),
  ('estructurasControl -> estrucWhile','estructurasControl',1,'p_estructurasControl','sintactico.py',16),
  ('operadorMat -> IGUAL','operadorMat',1,'p_operadorMat','sintactico.py',20),
  ('operadorMat -> PLUS','operadorMat',1,'p_operadorMat','sintactico.py',21),
  ('operadorMat -> MINUS','operadorMat',1,'p_operadorMat','sintactico.py',22),
  ('operadorMat -> TIMES','operadorMat',1,'p_operadorMat','sintactico.py',23),
  ('operadorLog -> AND','operadorLog',1,'p_operadorLog','sintactico.py',27),
  ('operadorLog -> OR','operadorLog',1,'p_operadorLog','sintactico.py',28),
  ('estrucIf -> IF logica cuerpo END','estrucIf',4,'p_estrucIf','sintactico.py',34),
  ('estrucIf -> IF logica cuerpo estrucElse','estrucIf',4,'p_estrucIf','sintactico.py',35),
  ('logica -> condicion','logica',1,'p_logica','sintactico.py',41),
  ('logica -> condicion operadorLog logica','logica',3,'p_logica','sintactico.py',42),
  ('condicion -> comparador COMPARACION comparador','condicion',3,'p_condicion','sintactico.py',48),
  ('condicion -> boolean','condicion',1,'p_condicion','sintactico.py',49),
  ('comparador -> VARIABLE','comparador',1,'p_comparador','sintactico.py',55),
  ('comparador -> primitivo','comparador',1,'p_comparador','sintactico.py',56),
  ('estrucElse -> ELSE cuerpo END','estrucElse',3,'p_estrucElse','sintactico.py',63),
  ('estrucElse -> ELSE logica cuerpo END','estrucElse',4,'p_estrucElse','sintactico.py',64),
  ('estrucWhile -> WHILE logica cuerpo END','estrucWhile',4,'p_estrucWhile','sintactico.py',70),
  ('cuerpo -> declaracion','cuerpo',1,'p_cuerpo','sintactico.py',76),
  ('cuerpo -> declaracion cuerpo','cuerpo',2,'p_cuerpo','sintactico.py',77),
  ('cuerpo -> cuerpo RETURN retornos','cuerpo',3,'p_cuerpo','sintactico.py',78),
  ('retornos -> VARIABLE','retornos',1,'p_retornos','sintactico.py',84),
  ('retornos -> primitivo','retornos',1,'p_retornos','sintactico.py',85),
  ('retornos -> expresion','retornos',1,'p_retornos','sintactico.py',86),
  ('retornos -> asignacion','retornos',1,'p_retornos','sintactico.py',87),
  ('declaracion -> VARIABLE IGUAL asignacion','declaracion',3,'p_declaracion','sintactico.py',93),
  ('declaracion -> VARIABLE IGUAL asignacion declaracion','declaracion',4,'p_declaracion','sintactico.py',94),
  ('declaracion -> VARIABLE operadorMat IGUAL opcion','declaracion',4,'p_declaracion','sintactico.py',95),
  ('declaracion -> VARIABLE operadorMat IGUAL opcion declaracion','declaracion',5,'p_declaracion','sintactico.py',96),
  ('opcion -> VARIABLE','opcion',1,'p_opcion','sintactico.py',100),
  ('opcion -> NUMBER','opcion',1,'p_opcion','sintactico.py',101),
  ('declaracion -> DEF VARIABLE LPAREN params RPAREN cuerpo END','declaracion',7,'p_declaracion_funcion','sintactico.py',107),
  ('params -> rubyParams','params',1,'p_params','sintactico.py',112),
  ('params -> rubyParams COMA params','params',3,'p_params','sintactico.py',113),
  ('rubyParams -> VARIABLE','rubyParams',1,'p_rubyParams','sintactico.py',120),
  ('rubyParams -> boolean','rubyParams',1,'p_rubyParams','sintactico.py',121),
  ('rubyParams -> NUMBER','rubyParams',1,'p_rubyParams','sintactico.py',122),
  ('asignacion -> primitivo','asignacion',1,'p_asignacion_primitivo','sintactico.py',127),
  ('asignacion -> HASH','asignacion',1,'p_asignacion_hash','sintactico.py',131),
  ('asignacion -> ARREGLO','asignacion',1,'p_asignacion_arreglo','sintactico.py',135),
  ('asignacion -> FICHERO','asignacion',1,'p_asignacion_fichero','sintactico.py',139),
  ('asignacion -> expresion','asignacion',1,'p_asignacion_expresion','sintactico.py',144),
  ('asignacion -> STRING','asignacion',1,'p_asignacion_string','sintactico.py',148),
  ('expresion -> NUMBER PLUS NUMBER','expresion',3,'p_expresion_suma','sintactico.py',153),
  ('expresion -> NUMBER MINUS NUMBER','expresion',3,'p_expresion_resta','sintactico.py',158),
  ('expresion -> termino','expresion',1,'p_expresion_term','sintactico.py',163),
  ('termino -> termino TIMES factor','termino',3,'p_termino_multi','sintactico.py',168),
  ('termino -> termino DIVIDE factor','termino',3,'p_termino_div','sintactico.py',173),
  ('termino -> factor','termino',1,'p_termino_factor','sintactico.py',178),
  ('factor -> NUMBER','factor',1,'p_factor_number','sintactico.py',183),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor_expresion','sintactico.py',188),
  ('primitivo -> NUMBER PUNTO NUMBER','primitivo',3,'p_primitivo_flotante','sintactico.py',193),
  ('primitivo -> NUMBER','primitivo',1,'p_primitivo_number','sintactico.py',198),
  ('primitivo -> boolean','primitivo',1,'p_primitivo_booleano','sintactico.py',203),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactico.py',208),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactico.py',209),
]
