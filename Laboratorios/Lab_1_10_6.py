digitos = {"0":["###", "# #", "# #", "# #", "###"]
         , "1":["  #", "  #", "  #", "  #", "  #"]
         , "2":["###", "  #", "###", "#  ", "###"]
         , "3":["###", "  #", "###", "  #", "###"]
         , "4":["# #", "# #", "###", "  #", "  #"]
         , "5":["###", "#  ", "###", "  #", "###"]
         , "6":["###", "#  ", "###", "# #", "###"]
         , "7":["###", "  #", "  #", "  #", "  #"]
         , "8":["###", "# #", "###", "# #", "###"]
         , "9":["###", "# #", "###", "  #", "###"]}

panel_in = input("Ingrese Número a representar en el panel")
panel_out = ['', '', '', '', '']

#Composicion de las cadenas que formaran la "visualizacion" final
for ndx in range(5):
    for ix in range(len(panel_in)):
        panel_out[ndx] += digitos.get(panel_in[ix])[ndx] + '   '
    
for i in range(5):
    print(panel_out[i])
    