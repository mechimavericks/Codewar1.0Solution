//Back-end complete function Template for C++
class Solution{
    public:
    int min_lights(int hallway[], int n)
{
    vector<pair<int,int>> lights;
    for(int i=0; i<n; i++)
        if(hallway[i] > -1)
            lights.push_back( pair<int,int> ( i-hallway[i], i+hallway[i] ) );
    
    sort(lights.begin(), lights.end());
    
    int target=0, lights_on=0, i=0;
    while(target<n)
    {
        if(i==lights.size() || lights[i].first>target)
            return -1;
        
        int max_range = lights[i].second;
        while( i+1<lights.size() && lights[i+1].first<=target )
        {
            i++;
            max_range = max( max_range,  lights[i].second );
        }
        if(max_range<target)
            return -1;
        
        lights_on++;
        target = max_range +1;
        i++;
    }
    
    return lights_on;
}
};
