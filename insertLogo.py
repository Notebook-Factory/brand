def insertLogo(fig,scX,scY,posX,posY,imXshift,imYshift):   
    fig.layout.images = [dict(source="https://raw.githubusercontent.com/notebook-factory/brand/main/nlibre_custom2.svg",xref="paper", yref="paper",x=posX+imXshift, y=posY+imYshift,
                sizex=scX , sizey=scY, opacity = 0.9)]
    fig.add_annotation(x=posX,y=posY,xref="paper",yref="paper",text="<a href=\"https://neurolibre.com\" target=\"_blank\" style=\"color:gray!important\">NeuroLibre</a>",
               showarrow = False, font=dict(size=8, color="gray"))

    return fig
