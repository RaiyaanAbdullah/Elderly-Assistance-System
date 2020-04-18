import React, { Component, Fragment } from "react";
import { ResponsiveBar } from '@nivo/bar';
// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.
// website examples showcase many properties,
// you'll often use just a few of them.


const MyResponsiveBar = ({ data /* see data tab */ }) => (
    <ResponsiveBar
    data={[
        {
        "country": "AD",
        "hot dog": 138,
        "hot dogColor": "hsl(334, 70%, 50%)",
        "burger": 39,
        "burgerColor": "hsl(35, 70%, 50%)",
        "sandwich": 94,
        "sandwichColor": "hsl(83, 70%, 50%)",
        "kebab": 73,
        "kebabColor": "hsl(268, 70%, 50%)",
        "fries": 104,
        "friesColor": "hsl(19, 70%, 50%)",
        "donut": 106,
        "donutColor": "hsl(87, 70%, 50%)"
        },
        {
        "country": "AE",
        "hot dog": 108,
        "hot dogColor": "hsl(142, 70%, 50%)",
        "burger": 163,
        "burgerColor": "hsl(84, 70%, 50%)",
        "sandwich": 137,
        "sandwichColor": "hsl(47, 70%, 50%)",
        "kebab": 123,
        "kebabColor": "hsl(17, 70%, 50%)",
        "fries": 132,
        "friesColor": "hsl(122, 70%, 50%)",
        "donut": 194,
        "donutColor": "hsl(228, 70%, 50%)"
        },
        {
        "country": "AF",
        "hot dog": 104,
        "hot dogColor": "hsl(278, 70%, 50%)",
        "burger": 146,
        "burgerColor": "hsl(138, 70%, 50%)",
        "sandwich": 7,
        "sandwichColor": "hsl(206, 70%, 50%)",
        "kebab": 159,
        "kebabColor": "hsl(343, 70%, 50%)",
        "fries": 89,
        "friesColor": "hsl(46, 70%, 50%)",
        "donut": 77,
        "donutColor": "hsl(152, 70%, 50%)"
        },
        {
        "country": "AG",
        "hot dog": 99,
        "hot dogColor": "hsl(309, 70%, 50%)",
        "burger": 54,
        "burgerColor": "hsl(55, 70%, 50%)",
        "sandwich": 107,
        "sandwichColor": "hsl(254, 70%, 50%)",
        "kebab": 84,
        "kebabColor": "hsl(216, 70%, 50%)",
        "fries": 86,
        "friesColor": "hsl(357, 70%, 50%)",
        "donut": 149,
        "donutColor": "hsl(226, 70%, 50%)"
        },
        {
        "country": "AI",
        "hot dog": 10,
        "hot dogColor": "hsl(86, 70%, 50%)",
        "burger": 56,
        "burgerColor": "hsl(93, 70%, 50%)",
        "sandwich": 94,
        "sandwichColor": "hsl(116, 70%, 50%)",
        "kebab": 4,
        "kebabColor": "hsl(94, 70%, 50%)",
        "fries": 186,
        "friesColor": "hsl(324, 70%, 50%)",
        "donut": 171,
        "donutColor": "hsl(35, 70%, 50%)"
        },
        {
        "country": "AL",
        "hot dog": 81,
        "hot dogColor": "hsl(244, 70%, 50%)",
        "burger": 145,
        "burgerColor": "hsl(358, 70%, 50%)",
        "sandwich": 130,
        "sandwichColor": "hsl(291, 70%, 50%)",
        "kebab": 189,
        "kebabColor": "hsl(179, 70%, 50%)",
        "fries": 63,
        "friesColor": "hsl(114, 70%, 50%)",
        "donut": 88,
        "donutColor": "hsl(210, 70%, 50%)"
        },
        {
        "country": "AM",
        "hot dog": 190,
        "hot dogColor": "hsl(58, 70%, 50%)",
        "burger": 138,
        "burgerColor": "hsl(37, 70%, 50%)",
        "sandwich": 114,
        "sandwichColor": "hsl(183, 70%, 50%)",
        "kebab": 37,
        "kebabColor": "hsl(160, 70%, 50%)",
        "fries": 174,
        "friesColor": "hsl(253, 70%, 50%)",
        "donut": 176,
        "donutColor": "hsl(205, 70%, 50%)"
        }
    ]}

    keys={[ 'hot dog', 'burger', 'sandwich', 'kebab', 'fries', 'donut' ]}
    indexBy="country"
    margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
    padding={0.3}
    colors={{ scheme: 'nivo' }}
    defs={[
        {
            id: 'dots',
            type: 'patternDots',
            background: 'inherit',
            color: '#38bcb2',
            size: 4,
            padding: 1,
            stagger: true
        },
        {
            id: 'lines',
            type: 'patternLines',
            background: 'inherit',
            color: '#eed312',
            rotation: -45,
            lineWidth: 6,
            spacing: 10
        }
    ]}
    fill={[
        {
            match: {
                id: 'fries'
            },
            id: 'dots'
        },
        {
            match: {
                id: 'sandwich'
            },
            id: 'lines'
        }
    ]}
        keys={[ 'hot dog', 'burger', 'sandwich', 'kebab', 'fries', 'donut' ]}
        indexBy="country"
        margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
        padding={0.3}
        colors={{ scheme: 'nivo' }}
        defs={[
            {
                id: 'dots',
                type: 'patternDots',
                background: 'inherit',
                color: '#38bcb2',
                size: 4,
                padding: 1,
                stagger: true
            },
            {
                id: 'lines',
                type: 'patternLines',
                background: 'inherit',
                color: '#eed312',
                rotation: -45,
                lineWidth: 6,
                spacing: 10
            }
        ]}
        fill={[
            {
                match: {
                    id: 'fries'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'sandwich'
                },
                id: 'lines'
            }
        ]}
        borderColor="inherit:darker(1.2)"
        axisTop={null}
        axisRight={null}
        axisBottom={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'country',
            legendPosition: 'middle',
            legendOffset: 32
        }}
        axisLeft={null}
        labelSkipWidth={12}
        labelSkipHeight={12}
        //labelTextColor="#737373"
        labelTextColor="inherit:darker(0.1)"
        legends={[
            {
                dataFrom: 'keys',
                anchor: 'bottom-right',
                direction: 'column',
                justify: false,
                translateX: 120,
                translateY: 0,
                itemsSpacing: 2,
                itemWidth: 100,
                itemHeight: 20,
                itemDirection: 'left-to-right',
                itemOpacity: 0.85,
                symbolSize: 20,
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemOpacity: 1
                        }
                    }
                ]
            }
        ]}
        animate={true}
        motionStiffness={90}
        motionDamping={15}
    />
)

export default MyResponsiveBar;