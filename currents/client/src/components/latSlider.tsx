import React, { useState } from 'react';

const CustomSlider: React.FC = () => {
    const [value, setValue] = useState<number>(30);

    const handleSliderChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setValue(Number(event.target.value));
        showSliderValue();
    };

    const showSliderValue = () => {
        console.log(`Latitude: ${value}`);
    };

    return (
        <div style={{ width: '300px', margin: 'auto', textAlign: 'center', padding: '20px', position: 'relative' }}>
            <label style={{ fontWeight: 'bold', marginBottom: '10px', display: 'block' }}>Latitude</label>

            <input
                type="range"
                min="24"
                max="37"
                step="1"
                value={value}
                onChange={handleSliderChange}
                style={{
                    width: '100%',
                    appearance: 'none',
                    height: '10px',
                    background: '#DDDDDD',
                    borderRadius: '5px',
                    outline: 'none',
                    cursor: 'pointer',
                    transition: 'background 0.15s ease-in-out',
                }}
            />

            <style>
                {`
                    input[type="range"]::-webkit-slider-thumb {
                        appearance: none;
                        width: 20px;
                        height: 20px;
                        border-radius: 50%;
                        background-color: #5858a3;
                        cursor: pointer;
                        border: 2px solid #ffffff;
                        box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
                    }
                `}
            </style>

            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '15px', fontSize: '14px' }}>
                <span style={{ position: 'relative', left: '-5px' }}>24°</span>
                <span>Selected: {value}</span>
                <span style={{ position: 'relative', right: '-5px' }}>37°</span>
            </div>
        </div>
    );
}

export default CustomSlider;
