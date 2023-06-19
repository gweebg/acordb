export const convertDate = (inputDate) => {

    // Split the date and time parts
    const [time, date] = inputDate.split(" ");

    // Split the date into day, month, and year
    const [day, month, year] = date.split("/");

    // Create a new Date object
    const formattedDate = new Date(`${month}/${day}/${year}`);

    // Get the month as a number (0-11)
    const monthIndex = formattedDate.getMonth();

    // Array of month abbreviations
    const monthAbbreviations = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ];

    // Get the abbreviated month string
    const abbreviatedMonth = monthAbbreviations[monthIndex];

    // Format the date string
    return `${day} ${abbreviatedMonth} ${year}`;
}