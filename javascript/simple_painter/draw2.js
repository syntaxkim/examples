document.addEventListener('DOMContentLoaded', () => {

    // state
    let draw = false;

    // 2 arrays and null value.
    let points = [];
    let lines = [];
    let svg = null;

    function render() {

        // Create the selection area.
        svg = d3.select('#draw')
        .attr('height', window.innerHeight)
        .attr('width', window.innerWidth);

        svg.on('mousedown touchstart', function() {
            draw = true;
            const coords = d3.mouse(this);
            draw_point(coords[0], coords[1], false);
        });

        svg.on('mouseup touchend', () => {
            draw = false;
        });

        svg.on('mousemove touchmove', function() {
            if (draw === false)
                return;
            const coords = d3.mouse(this);
            draw_point(coords[0], coords[1], true);
        });

        document.querySelector('#erase').onclick = () => {
            for (let i = 0; i < points.length; i++)
                points[i].remove();
            for (let i = 0; i < lines.length; i++)
                lines[i].remove();
            points = [];
            lines = [];
        }
    }

    function draw_point(x, y, connect) {

        const color = document.querySelector('#color-picker').value;
        const thickness = document.querySelector('#thickness-picker').value;

        // If connecting points is needed,
        if (connect) {
            // Get the most recent point drawn, that is, the last element of the array 'points'.
            const last_point = points[points.length - 1];
            // Draw a line that's going to connent those points.
            const line = svg.append('line')
            .attr('x1', last_point.attr('cx'))
            .attr('y1', last_point.attr('cy'))
            .attr('x2', x)
            .attr('y2', y)
            .attr('stroke-width', thickness * 2)
            .style('stroke', color);
            // Add the line to the array 'lines'.
            lines.push(line);
        }

        const point = svg.append('circle')
        .attr('cx', x)
        .attr('cy', y)
        .attr('r', thickness)
        .style('fill', color);

        // Add the point to the array 'points'.
        points.push(point);
    }

    render();
});