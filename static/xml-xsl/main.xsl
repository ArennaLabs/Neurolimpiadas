<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" encoding="UTF-8" doctype-public="-//W3C//DTD HTML 4.01 Transitional//EN"/>

  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" href="../styles/main.css"/>
        <style>
        
        </style>
        
      </head>
      <body>
        <div class="theme theme-dark">
          <div class="bracket disable-image">
            <xsl:for-each select="torneo/ronda">
              <xsl:variable name="lineLength" select="112 * position()"/>
              <div class="column one">
                <xsl:if test="@final">
                  <xsl:attribute name="id">
                    <xsl:value-of select="@final"/>
                  </xsl:attribute>
                </xsl:if>    
                    <xsl:for-each select="partido">
                      <div class="match">
                        <xsl:attribute name="ronda">
                          <xsl:value-of select="@ronda"/>
                        </xsl:attribute>
                        <xsl:attribute name="id_partido">
                          <xsl:value-of select="@id"/>
                        </xsl:attribute>
                        
                        <xsl:for-each select="equipo">
                          <div class="team">
                            <xsl:attribute name="id">
                              <xsl:value-of select="@tipo"/>
                            </xsl:attribute>
                            <!-- <span class="seed"><xsl:value-of select="@id"/></span> -->
                            <img>
                              <xsl:attribute name="src">
                                <xsl:value-of select="@imagen"/>
                              </xsl:attribute>
                            </img>
                            <span class="name"><xsl:value-of select="@nombre"/></span>
                            <!-- <span class="score" id="hola"><xsl:value-of select="@puntos"/></span> -->
                          </div>
                        </xsl:for-each>
                        <!-- <div class="match-lines">
                          <div class="line one"></div>
                          <div class="line two" style="height: {$lineLength}px"></div>
                        </div>
                        <div class="match-lines alt">
                          <div class="line one"></div>
                        </div> -->
                      </div>
                    </xsl:for-each>
                </div>
            </xsl:for-each>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
