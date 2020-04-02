
    <div id='map' style='width: 700px; height: 700px;'></div>
    <script>
        mapboxgl.accessToken = 'pk.eyJ1IjoibWFjazY2aG0iLCJhIjoiY2s4ZXowYnJmMDFseDNmcGhjbmg4ODc4cyJ9.17aD7Ep5mTEgYqTSKkwzUw';
        var map = new mapboxgl.Map({
            container: 'map', // container id
            style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
            center: [{{ catch.longitude }}, {{ catch.latitude }}] // starting position [lng, lat]
        zoom: 11 // starting zoom
        });
    </script>
  