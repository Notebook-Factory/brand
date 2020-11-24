def insertLogo(fig,scX,scY,posX,posY):
    fig.layout.images = [dict(source="https://raw.githubusercontent.com/notebook-factory/brand/main/neurolibre-icon-red.png",xref="paper", yref="paper",x=posX, y= posY,
            sizex=scX, sizey=scY, opacity = 0.8)]
    fig.add_annotation(x=posX,y=posY+0.1,xref="paper",yref="paper",text="<a href=\"https://neurolibre.com\" target=\"_blank\" style=\"color:gray!important\">NeuroLibre</a>",
           showarrow = False, font=dict(size=8, color="gray"))
    return fig
