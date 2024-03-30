document.addEventListener("DOMContentLoaded", function () {
    var ctx1 = document.getElementById("dounghtChart1").getContext("2d");
    var ctx2 = document.getElementById("dounghtChart2").getContext("2d");
    var ctx3 = document.getElementById("areaChart").getContext("2d");
    var ctx4 = document.getElementById("barChart").getContext("2d");
    var chart1 = new Chart(ctx1, {
        type: 'doughnut',
        data: {
            labels: ["Pending", "Reviewed", "Re-Reviw"],
            datasets: [{
                data: [20, 70, 10],
                backgroundColor: [
                    '#7cb5ec',
                    '#434348',
                    '#90ed7d'
                ],
                borderColor: 'transparent',
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 1,
            cutout: '65%',
            legend: {
                display: false,
            },
            animation: {
                animateScale: true,
                animateRotate: true
            }
        }
    });
    var chart2 = new Chart(ctx2, {
        type: 'doughnut',
        data: {
            labels: ["Open", "Responded", "Closed"],
            datasets: [{
                data: [30, 18, 12],
                backgroundColor: [
                    '#7cb5ec',
                    '#434348',
                    '#90ed7d'
                ],
                borderColor: 'transparent',
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 1,
            cutout: '65%',
            legend: {
                display: false,
            },
            animation: {
                animateScale: true,
                animateRotate: true
            }
        }
    });
    var chart3 = new Chart(ctx3, {
        type: 'line',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [{
                label: 'Chart Recieve',
                data: [120, 160, 133, 140, 150, 200, 350, 111, 220, 250, 170, 190],
                backgroundColor: '#bddaf5',
                borderColor: '#7cb5ec',
                borderWidth: 2,
                pointBackgroundColor: '#7cb5ec',
                pointBorderColor: '#7cb5ec',
                pointRadius: 3,
                pointHoverRadius: 3,
                fill: true,
                tension: 0.4,
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 2.5,
            legend: {
                display: false,
            },
            scales: {
                x: {
                    display: true,
                    grid: {
                        display: false,
                    },
                    ticks: {
                        display: true,
                    }
                },
                y: {
                    display: false,
                    suggestedMin: 0,
                    suggestedMax: 500,
                }
            },
            plugins: {
                tooltip: {
                    mode: 'index',
                    intersect: false,
                }
            }
        }
    });
    var chart4 = new Chart(ctx4, {
        type: 'bar',
        data: {
            labels: ["Facility1", "Facility2", "Facility3", "Facility4", "Facility5", "Facility6", "Facility7", "Facility8", "Facility9"],
            datasets: [{
                label: "Facility",
                data: [380, 300, 180, 250, 210, 190, 170, 270, 190],
                backgroundColor: '#7cb5ec',
                borderColor: 'transparent',
                borderWidth: 1,
                barThickness: 40,
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 2.5,
            legend: {
                display: false,
            },
            scales: {
                x: {
                    display: true,
                    grid: {
                        display: false,
                    },
                    ticks: {
                        display: true,
                    }
                },
                y: {
                    display: true,
                    grid: {
                        display: false,
                    },
                    ticks: {
                        display: true,
                    },
                    suggestedMin: 0,
                    suggestedMax: 500,
                }
            },
            plugins: {
                tooltip: {
                    mode: 'index',
                    intersect: false,
                }
            }
        }
    });
});
