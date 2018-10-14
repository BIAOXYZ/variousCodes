#include <stdio.h>
#include <math.h>

int main()
{
    float xCenter, yCenter, radius;
    scanf("%f %f %f", &xCenter, &yCenter, &radius);

    int xCoordinate, yCoordinate, final_x, final_y;
    int mini_x, mini_y, maxi_x, maxi_y;
    float distance;

    distance = sqrt( (xCoordinate-xCenter)*(xCoordinate-xCenter)+(yCoordinate-yCenter)*(yCoordinate-yCenter) );
    mini_x = ceil(xCenter - radius);
    mini_y = ceil(yCenter - radius);
    maxi_x = ceil(xCenter + radius);
    maxi_y = ceil(yCenter + radius);

    for (xCoordinate = mini_x, yCoordinate = mini_y;
         (distance <= radius && xCoordinate <= maxi_x && yCoordinate = maxi_y) != 0;
         xCoordinate++, yCoordinate++)
        {
            if ( distance <= sqrt( (xCoordinate-xCenter)*(xCoordinate-xCenter)+(yCoordinate-yCenter)*(yCoordinate-yCenter) ) )
                {
                    distance = sqrt( (xCoordinate-xCenter)*(xCoordinate-xCenter)+(yCoordinate-yCenter)*(yCoordinate-yCenter) );
                    final_x = xCoordinate;
                    final_y = yCoordinate;
                }
        }
    printf("%d %d\n", final_x, final_y);
    return 0;
}
